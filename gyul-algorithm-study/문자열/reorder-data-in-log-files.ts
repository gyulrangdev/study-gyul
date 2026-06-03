function reorderLogFiles(logs: string[]): string[] {
  const letterLog = [];
  const digitLog = [];

  for (const log of logs) {
    const [id, ...rest] = log.split(" ");

    if (isNaN(Number(rest[0]))) {
      letterLog.push(log);
    } else {
      digitLog.push(log);
    }
  }

  letterLog.sort((a, b) => {
    const [aId, ...aContent] = a.split(" ");
    const [bId, ...bContent] = b.split(" ");
    let aContentString = aContent.join(" ");
    let bContentString = bContent.join(" ");

    if (aContentString === bContentString) {
      return aId.localeCompare(bId);
    }

    return aContentString.localeCompare(bContentString);
  });

  return [...letterLog, ...digitLog];
}
