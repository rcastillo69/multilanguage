const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var allocator = std.heap.page_allocator;

    const stdin = std.io.getStdIn().reader();

    try stdout.print("Enter temperature in Fahrenheit: ", .{});

    const input = try stdin.readLineAlloc(allocator, 100, true);

    // Convert the input to a float
    var temperature = try std.fmt.parseFloat(f32, input);

    // Convert the temperature from Fahrenheit to Celsius
    var celsius = (temperature - 32) * (5.0 / 9.0);

    // Print the result
    try stdout.print("The temperature in Celsius is: {} °C\n", .{celsius});

    defer allocator.free(input);
}
