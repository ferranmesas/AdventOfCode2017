let get_line_value_part1: int list -> int = fun l ->
  match l with
  | x::xs -> (List.fold_left max x xs) - (List.fold_left min x xs)
  | [] -> 0;;

let int_list_of_str s =
  let s = (Str.split (Str.regexp "[ \t]") s) in 
  List.map int_of_string s;;

let evenly_divides num den =
  num <> den && num = (num / den) * den 

let find_value lst num =
  try
    let v = List.find (evenly_divides num) lst in
    num / v
  with Not_found ->
    0

let get_line_value_part2 l =
  List.find ((<) 0) (List.map (find_value l) l);;

let main = 
  let total = ref 0 in
  try
    while true do
      let num = get_line_value_part2 (int_list_of_str (read_line ())) in
      total := !total + num
    done
  with End_of_file ->
    print_int !total