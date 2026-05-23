# aTan's THORN-2 RISC-V CPU Project

## What?

This is an implementation of the RISC-V spec using nothing but basic logic and
memory elements. 

The project has been inspired by several similar projects, most
notably [Robert Baruch's LMARV-1](https://www.youtube.com/playlist?list=PLEeZWGE3PwbansoxKjjMKHQqS_2cm8i60),
[James Sharman's JAM-1](https://www.youtube.com/playlist?list=PLFhc0MFC8MiCDOh3cGFji3qQfXziB9yOw)
and [Fabian Schuiki's Superscalar CPU](https://www.youtube.com/playlist?list=PLyR4neQXqQo5nPdEiMbaEJxWiy_UuyNN4).

As of May '26 I'm looking to implement the RV64I spec, with vague plans to 
extend this with the M and maybe F modules. I don't have any timeframe for that
though.

## Why?

IDK. It's fun :)

## That's mental... Where can I see the details?

If you go to `Docs/Writeup/` you can see a proper typewritten rundown on how
everything works and my "design process". There's quite a bit of techy stuff
there, and it's not _guaranteed_ to make sense - it's mostly a document to help
me keep track of what I'm doing between each section.

## Where are the schematics?

See `Schematics/`. This will be spotty for a while yet.

## Can I do anything with this project?

Please do! Though do read the license first. Broadly speaking, keep everything
open-source and don't be evil :)

## What happened to the THORN-1?

¬_¬ it went wrong...

In reality, it was the same as this project, but massively overcomplicated and
everything I learned there helped make this version much simpler. T1 used
pipelined ram for the registers, leading to a 4-phase clock and massive pain in
the ALU, so I abandoned it to start over.

-aTan 2026
