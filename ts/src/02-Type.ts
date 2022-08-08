"use strict";
/**
 * Self executing anonymous function using TS.
 */
(()=> {
  // This a constant
  const myConstant = "This is a constant";
  console.log(myConstant);

  // Call string function
  console.log(myConstant.toLowerCase());

  /*
     Primitives
  */
/**
   String
*/

 // Explicit declaration
 let myString: string = "default string";
 console.log(myString);

 // Implicit declaration
 let myString2 = "default string2";
 console.log(myString2);

 /**
   Number
*/

 // Explicit declaration
 let number1: number = 100;
 console.log(number1);

 // Implicit declaration
 let number2 = 200;
 console.log(number2);

  /**
   Boolean declaration
  */

  // Implicit declaration
  let isValid = false;
  console.log(isValid);

  /*
    Enum
  */

    enum Direction {
      Up = 1,
      Down,
      Left,
      Right,
    }
    console.log("Enum");
    console.log(Direction);
    console.log(Direction.Up);

    /*
      Special values
    */

    /*
      Values of Null and Undefined
      Both represent no value or absence of any value.
    */

      // Undefined value
      let foo:any;
      console.log(foo);         //undefined

      // Null value
      let b:null=null
      console.log(b);

      /*
      any is a type that disables type checking and effectively allows all types to be used.
      */
      console.log("Any");
      let v: any = true;
      v = "a string"; // no error as it can be "any" type
      console.log(v);

      // Multiple and group of dclarations are not allowed

      /*
        Casting
      */

        // Casting with as
        let x:unknown = 4;
       console.log((x as string).length);

       let x2 = 44;
      console.log(((x2 as unknown) as number));

      // Determine the type of the value

      let y2 = 44;
      console.log(typeof y2);


})();


