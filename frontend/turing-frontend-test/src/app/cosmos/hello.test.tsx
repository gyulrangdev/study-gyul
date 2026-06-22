import { render } from "@testing-library/react";
import { renderToString } from "react-dom/server";
import helloStory from "./Hello.fixture";
import { test, expect } from "vitest";
import { expectTL } from "../../siheom/expectTL";
import { queryTL } from "../../siheom/queryTL";

test("render hello", async () => {
  render(helloStory);
  await expectTL(queryTL.heading("Hello World")).toBeVisible();
});

test("adds 1 + 2 to equal 3", () => {
  expect(1 + 2).toBe(3);
});

test("render hello", () => {
  document.body.innerHTML = renderToString(helloStory);
  expect(document.body.innerHTML).toBe("<h1>Hello World!</h1>");
});
