const std = @import("std");
const io = std.io.getStdOut().writer();

pub fn main() !void {
    // Integer types
    var myInt: i32 = 10;
    try io.print("Integer: {}\n", .{myInt});

    // Unsigned integer type
    var myUint: u32 = 300;
    try io.print("Unsigned Integer: {}\n", .{myUint});

    // Float type
    var myFloat: f32 = 3.14;
    try io.print("Float: {}\n", .{myFloat});

    // Double type
    var myDouble: f64 = 9.82;
    try io.print("Double: {}\n", .{myDouble});

    // Boolean type
    var myBool: bool = true;
    try io.print("Boolean: {}\n", .{myBool});

    // Character type
    var myChar: u8 = 'A'; // Characters are represented by u8 in Zig
    try io.print("Character: {}\n", .{myChar});

    // Struct example
    const MyStruct = struct {
        field1: i32,
        field2: bool,
    };
    var myStruct = MyStruct{ .field1 = 123, .field2 = false };
    try io.print("Struct: {{.field1 = {}, .field2 = {}}}\n", .{ myStruct.field1, myStruct.field2 });

    // Complex number (imaginary) example
    const Complex = struct {
        real: f64,
        imag: f64,
    };
    var myComplex = Complex{ .real = 1.0, .imag = 2.0 };
    try io.print("Complex Number: {{.real = {}, .imag = {}}}\n", .{ myComplex.real, myComplex.imag });
}
