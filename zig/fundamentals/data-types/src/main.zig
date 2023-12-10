const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    var input: f32 = try ask_user();

    // Convert the input to a float
    var temperature = try std.fmt.parseFloat(f32, input);

    // Convert the temperature from Fahrenheit to Celsius
    var celsius = (temperature - 32) * (5.0 / 9.0);

    // Print the result
    try stdout.print("The temperature in Celsius is: {} °C\n", .{celsius});
}

fn ask_user() !f32 {
    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();

    var buf: [10]f32 = undefined;

    try stdout.print("A number please: ", .{});

    if (try stdin.readUntilDelimiterOrEof(buf[0..], '\n')) |user_input| {
        return std.fmt.parseInt(f32, user_input, 10);
    } else {
        return @as(f32, 0);
    }
}
