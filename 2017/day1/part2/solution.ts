import { readFileSync } from "fs";

function solveCaptcha(input: string): number {
  const digits = input.trim();
  let sum = 0;
  const halfLength = digits.length / 2;

  for (let i = 0; i < digits.length; i++) {
    const current = digits[i];
    const halfway = digits[(i + halfLength) % digits.length]; 

    if (current === halfway) {
      sum += parseInt(current, 10);
    }
  }

  return sum;
}

const input = readFileSync("../input.txt", "utf-8");
const result = solveCaptcha(input);

console.log(`Answer: ${result}`);

