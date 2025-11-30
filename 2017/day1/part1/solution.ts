import { readFileSync } from "fs";

function solveCaptcha(input: string): number {
  const digits = input.trim();
  let sum = 0;

  for (let i = 0; i < digits.length; i++) {
    const current = digits[i];
    const next = digits[(i + 1) % digits.length]; 

    if (current === next) {
      sum += parseInt(current, 10);
    }
  }

  return sum;
}

const input = readFileSync("../input.txt", "utf-8");
const result = solveCaptcha(input);

console.log(`Answer: ${result}`);

