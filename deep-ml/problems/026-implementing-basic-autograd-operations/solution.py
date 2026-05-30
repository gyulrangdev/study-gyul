class Value:
    def __init__(self, data, _children=(), _op=""):
        # 이 객체가 들고 있는 실제 숫자 값이다.
        self.data = data

        # 최종 출력값이 이 값에 얼마나 영향을 받는지 저장한다.
        # 처음에는 아직 backward를 하지 않았으므로 0에서 시작한다.
        self.grad = 0

        # 이 값을 만들 때 사용된 이전 Value들을 저장한다.
        # 예를 들어 a + b로 만든 값이면 _prev는 {a, b}가 된다.
        self._prev = set(_children)

        # 이 값을 만든 연산 이름이다. 계산에는 꼭 필요 없지만 그래프를 이해할 때 도움이 된다.
        self._op = _op

        # 각 연산마다 "내 grad를 부모들에게 어떻게 나눠줄지"를 나중에 여기에 저장한다.
        self._backward = lambda: None

    def __repr__(self):
        # print 했을 때 data와 grad를 같이 보이게 만든다.
        return f"Value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        # 숫자와 Value를 더하는 경우도 처리하기 위해 숫자는 Value로 감싼다.
        other = other if isinstance(other, Value) else Value(other)

        # forward 계산: 두 숫자를 더해서 새로운 Value를 만든다.
        # 동시에 이 결과가 self와 other에서 왔다는 그래프 연결도 저장한다.
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            # 덧셈에서는 out이 1만큼 바뀌면 self도 1만큼, other도 1만큼 책임이 있다.
            # 그래서 out.grad를 두 입력에 그대로 더해준다.
            self.grad += out.grad
            other.grad += out.grad

        # backward 때 실행할 책임 전달 규칙을 결과 노드에 붙여둔다.
        out._backward = _backward
        return out

    def __mul__(self, other):
        # 숫자와 Value를 곱하는 경우도 처리하기 위해 숫자는 Value로 감싼다.
        other = other if isinstance(other, Value) else Value(other)

        # forward 계산: 두 숫자를 곱해서 새로운 Value를 만든다.
        # 동시에 이 결과가 self와 other에서 왔다는 그래프 연결도 저장한다.
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            # 곱셈에서 self 쪽 책임은 other.data만큼 커진다.
            # 예를 들어 out = self * other 이면 d_out/d_self = other.data 이다.
            self.grad += other.data * out.grad

            # other 쪽 책임은 self.data만큼 커진다.
            # 예를 들어 out = self * other 이면 d_out/d_other = self.data 이다.
            other.grad += self.data * out.grad

        # backward 때 실행할 책임 전달 규칙을 결과 노드에 붙여둔다.
        out._backward = _backward
        return out

    def __radd__(self, other):
        # 2 + Value(...)처럼 Value가 오른쪽에 오는 덧셈도 지원한다.
        return self + other

    def __rmul__(self, other):
        # 2 * Value(...)처럼 Value가 오른쪽에 오는 곱셈도 지원한다.
        return self * other

    def relu(self):
        # forward 계산: 양수면 그대로 두고, 0 이하이면 0으로 막는다.
        out = Value(self.data if self.data > 0 else 0, (self,), "ReLU")

        def _backward():
            # ReLU는 forward 값이 양수였을 때만 gradient를 통과시킨다.
            # 0 이하였으면 출력이 막혔으므로 이전 값에도 책임을 넘기지 않는다.
            self.grad += (1 if self.data > 0 else 0) * out.grad

        # backward 때 실행할 책임 전달 규칙을 결과 노드에 붙여둔다.
        out._backward = _backward
        return out

    def backward(self):
        # backward는 최종 출력에서 시작해서 이전 값들로 책임을 거꾸로 전달해야 한다.
        # 그러려면 부모보다 자식이 먼저 처리되도록 topological order를 만든다.
        topo = []
        visited = set()

        def build_topo(node):
            # 이미 방문한 노드는 다시 처리하지 않는다.
            if node not in visited:
                visited.add(node)

                # 먼저 부모 노드들을 끝까지 방문한다.
                for child in node._prev:
                    build_topo(child)

                # 부모를 모두 넣은 뒤 현재 노드를 넣으면 topological order가 된다.
                topo.append(node)

        # self는 최종 출력 노드다. 여기서부터 그래프 전체를 모은다.
        build_topo(self)

        # 최종 출력은 자기 자신에 대해 1만큼 영향을 준다.
        # 즉 d_output / d_output = 1 이라서 backward 시작값은 1이다.
        self.grad = 1

        # topo는 입력 -> 출력 순서이므로, backward는 반대로 출력 -> 입력 순서로 돈다.
        for node in reversed(topo):
            # 각 노드에 저장된 local backward 규칙을 실행해서 부모들의 grad를 누적한다.
            node._backward()
