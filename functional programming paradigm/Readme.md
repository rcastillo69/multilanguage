# Concepts

## Defining Functional Programming

A paradigm is a framework that expresses a particular set of assumptions, relies on particular ways of thinking through problems, and uses particular methodologies to solve those problems

The main difference between the functional programming paradigm and other paradigms is that functional programs use math functions rather than statements

This difference means that rather than write a precise set of steps to solve a problem, you use math functions, and you don’t worry about how the language performs the task

This difference means that rather than write a precise set of steps to solve a problem, you use math functions, and you don’t worry about how the language performs the task.

As a result, calling a functional program function always produces the same result given a particular set of inputs, thereby making functional programs more predictable than those that support state.

Because functional programs don’t maintain state, the data they work with is also immutable, which means that you can’t change it. To change a variable’s value, you must create a new variable. Again, this makes functional programs more predictable than other approaches and could make functional programs easier to run on multiple processors

Understanding its goals
Imperative programming, the kind of programming that most developers have done until now, is akin to an assembly line, where data moves through a series of steps in a specific order to produce a particular result

Object-oriented programming (OOP) simply modularizes and hides the steps, but the underlying paradigm is the same.Even with modularization, OOP often doesn’t allow rearrangement of the object code in unanticipated ways because of the underlying interdependencies of the code.

Even with modularization, OOP often doesn’t allow rearrangement of the object code in unanticipated ways because of the underlying interdependencies of the code.

Using pure functions creates a flexible environment in which code order depends on the underlying math. That math models a real-world environment, and as our understanding of that environment changes and evolves, the math model and functional code can change with it — without the usual problems of brittleness that cause imperative code to fail. Modifying functional code is faster and less error prone because the person implementing the change must understand only the math and doesn’t need to know how the underlying code works. In addition, learning how to create functional code can be faster as long as the person understands the math model and its relationship to the real world.

## Some Common Paradigms
### You should know these:

- Imperative: Programming with an explicit sequence of commands that update state.

- Declarative: Programming by specifying the result you want, not how to get it.

- Structured: Programming with clean, goto-free, nested control structures.

- Procedural: Imperative programming with procedure calls.

- Functional (Applicative): Programming with function calls that avoid any global state.

- Function-Level (Combinator): Programming with no variables at all.

- Object-Oriented: Programming by defining objects that send messages to each other. Objects have their own internal (encapsulated) state and public interfaces. Object orientation can be:

    - Class-based: Objects get state and behavior based on membership in a class.
    - Prototype-based: Objects get behavior from a prototype object.

- Event-Driven: Programming with emitters and listeners of asynchronous actions.

- Flow-Driven: Programming processes communicating with each other over predefined channels.

- Logic (Rule-based): Programming by specifying a set of facts and rules. An engine infers the answers to questions.

- Constraint: Programming by specifying a set of constraints. An engine finds the values that meet the constraints.

- Aspect-Oriented: Programming cross-cutting concerns applied transparently.

- Reflective: Programming by manipulating the program elements themselves.

- Array: Programming with powerful array operators that usually make loops unnecessary.
Paradigms are not meant to be mutually exclusive; a single program can feature multiple paradigms!

In addition to using lambda functions, languages that implement the functional programming paradigm have some other features in common. Here is a quick overview of these features:

## Using Functional Programming to Perform Tasks

- First-class and higher-order functions: First-class and higher-order functions both allow you to provide a function as an input, as you would when using a higher-order function in calculus.

- Pure functions: A pure function has no side effects. When working with a pure function, you can

    * Remove the function if no other functions rely on its output
    * Obtain the same results every time you call the function with a given set of inputs
    * Reverse the order of calls to different functions without any change to application functionality
    * Process the function calls in parallel without any consequence
    * Evaluate the function calls in any order, assuming that the entire language doesn’t allow side effects

- Recursion: Functional language implementations rely on recursion to implement looping. In general, recursion works differently in functional languages because no change in application state occurs.

- Referential transparency: The value of a variable (a bit of a misnomer because you can’t change the value) never changes in a functional language implementation because functional languages lack an assignment operator.

## Some considerations

You often find a number of other considerations for performing tasks in functional programming language implementations, but these issues aren’t consistent across languages. For example, some languages use strict (eager) evaluation, while other languages use non-strict (lazy) evaluation. Under strict evaluation, the language fully checks the function before evaluating it. Even when a term within the function isn’t used, a failing term will cause the function as a whole to fail. However, under non-strict evaluation, the function fails only if the failing term is used to create an output. The Miranda, Clean, and Haskell languages all implement non-strict evaluation.

Various functional language implementations also use different type systems, so the manner in which the underlying computer detects the type of a value changes from language to language. In addition, each language supports its own set of data structures.