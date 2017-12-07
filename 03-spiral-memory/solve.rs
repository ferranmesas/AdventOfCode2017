fn main() {
	let mut numbers: Vec<i32> =
	    reader.read_line().unwrap().as_slice()
	        .split_whitespace()
	        .map(|s| s.parse().unwrap())
	        .collect();
	println!("{:?}", v2);
}