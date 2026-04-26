# aTan's THORN-2 RISC-V CPU Project

## What?

This is an implementation of the RISC-V spec using nothing but basic logic and
memory elements.

## Why?

IDK. It's fun :)

## That's mental... Where can I see the details?

If you go to `./Docs/Writeup/` you can see a proper typewritten rundown on how
everything works and my "design process". There's quite a bit of techy stuff
there and it's not _guaranteed_ to make sense - it's mostly a document to help
me keep track of what I'm doing between each section.

## Where are the schematics?

See `./Schematics`. This will be spotty for a while yet.

## What happened to THORN-1?

¬_¬ it went wrong...

In reality, it was the same as this project, but massively overcomplicated and
everything I learnt there helped make this version much simpler. T1 used
pipelined ram for the registers, leading to a 4-phase clock and massive pain in
the ALU, so I abandoned it to start over.

- aTan 2026
