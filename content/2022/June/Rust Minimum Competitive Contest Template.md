## Minimum Template

This is the minimum template that only implements `BufferedReader` and `BufferedWriter`. Unlike `std::io::BufReader`, you can simply use `sc.nextInt()` to get next int.

```rust
#![allow(non_snake_case)]
#![allow(dead_code)]
#![allow(unused_imports)]

fn slove(sc: &mut Scanner, wr: &mut Writer){
	// Your code starts here.
}

fn main() {
    let mut sc = Scanner::new();
    let mut wr = Writer::new();

    let T = sc.nextUsize();
    for _ in 0..T {
        slove(&mut sc, &mut wr);
    }
}

use std::{
    array,
    cmp::*,
    collections::{HashMap, LinkedList, VecDeque},
    hash::Hash,
    io::{stdin, stdout, BufRead, BufReader, BufWriter, Stdin, Stdout, Write},
};

struct Scanner {
    buf: LinkedList<String>,
    reader: BufReader<Stdin>,
}

impl Scanner {
    fn new() -> Scanner {
        Scanner {
            buf: LinkedList::new(),
            reader: BufReader::new(stdin()),
        }
    }

    fn read<T: std::str::FromStr>(&mut self) -> T {
        match self.buf.pop_front() {
            Some(s) => s.parse().ok().expect("failed while parsing"),
            None => {
                self.buf = self
                    .nextLine()
                    .split_whitespace()
                    .map(String::from)
                    .collect();
                self.read()
            }
        }
    }

    fn nextUsize(&mut self) -> usize {
        self.read()
    }

    fn nextInt(&mut self) -> i32 {
        self.read()
    }

    fn nextFloat(&mut self) -> f32 {
        self.read()
    }

    fn nextLine(&mut self) -> String {
        let mut buffer = String::new();
        self.reader.read_line(&mut buffer).ok();
        String::from(buffer.trim())
    }
}

struct Writer {
    writer: BufWriter<Stdout>,
}

impl Writer {
    fn new() -> Writer {
        Writer {
            writer: BufWriter::new(stdout()),
        }
    }

    fn print<T: ToString>(&mut self, s: &T) {
        self.writer.write(s.to_string().as_bytes()).ok();
    }

    fn println<T: ToString>(&mut self, s: &T) {
        self.print(s);
        self.print(&'\n');
    }
}
```
