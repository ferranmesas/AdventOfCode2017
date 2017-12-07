use std::io;
use std::collections::HashMap;

fn main() {
  let reader = io::stdin();
  let mut buffer = String::new();
  reader.read_line(&mut buffer).unwrap();
  let mut numbers: Vec<i32> = buffer
    .split_whitespace()
    .map(|s| s.parse().unwrap())
    .collect();

  let mut seen_states = HashMap::new();
  let mut iter_count = 0;

  let length = numbers.len();
  loop {
    if seen_states.contains_key(&numbers.clone()) {
      println!("{}", iter_count - seen_states[&numbers]);
      break;
    }
    seen_states.insert(numbers.clone(), iter_count);
    let biggest = *numbers.iter().max().unwrap();
    let index = numbers.iter().position(|x| *x == biggest).unwrap();
    numbers[index] = 0;
    for i in 0..biggest as usize {
      numbers[(1 + index + i) % length] += 1;
    }
    iter_count += 1;
  }
}