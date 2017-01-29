# Stepper motor

## How to connect it
- I am useing an driver for stepper motors with 4 chanels and another 2 pins for + and -.
- That 4 inputs IN1, IN2, IN3 and IN4 you need to connect on 4 gpio pins on raspberry pi.
- The other two: + one you need to connect it on 5v pin and the other one (-) on the ground pin.

## How it works.
A stepper motor has 4 coils. Each coil is controlled by you though that 4 channels that you
connected to gpio pins. In order to make a rotation the stepper motor need to go through all 4 coils.
That meas 4 steps for a rotation.

But in reality it cannot make 1 step only half a step. So in total it heeds to make 8 steps for a 
full rotation.

The stepper motor has also some gear that is going to make the rotation smoother.
Because of this we need to multiply the rotations with 64. that means 8 x 64 = 512.

So the stepper motor need in total 512 steps for a full rotation.

Now in order to write this, we need a matrix that has 8 rows (main steps) and 4 columns(the coils).

In order to rotate the motor we need to have two coils active in the same time for half steps(steps between the coils)
and one coil active for the other half step in this case to be oriented directly to the coil not between them.

You will see the example with this matrix in the code.

So for a full rotation we need to iterate 512 time x 8(steps) x 4(coils) in order to send
the right signals to the coils.

As you see there is a sleep in the code. With that you can controll the speed of the motor.
you will not be able to go much more faster than that because the motor cannot keep step with, 
but you can make it would slower.

Also if you want to reverse the rotation you will need to reverse the way you iterate through coils.
