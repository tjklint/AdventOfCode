open System.IO
open System

//  Check if it has all the fields.
let isPassportValid (passport: string) =
    let requiredFields = ["byr"; "iyr"; "eyr"; "hgt"; "hcl"; "ecl"; "pid"]
    requiredFields |> List.forall (fun field -> passport.Contains(field + ":"))

// Split the passport up into different parts
let splitIntoPassports (input: string) =
    input.Split([| "\n\n"; "\r\n\r\n" |], StringSplitOptions.RemoveEmptyEntries) // Last part removes all empty strings.

// Read the input file
let inputText = File.ReadAllText("day4input.txt")

// Split input into passports array.
let passports = splitIntoPassports inputText

// Count valid passports
let validPassports = passports |> Array.filter isPassportValid |> Array.length

printfn "Number of valid passports: %d" validPassports