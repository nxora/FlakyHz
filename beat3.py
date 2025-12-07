from studrel import *

bpm(140)  

# Main melody - piano + guitar
melody = stack(
    [
        seq([C4, D4, E4, C4, E4, E4, E4], dur=0.25)
        .sound("piano")
        .room(0.3),
        seq([E4, D4, C4, D4, E4, E4, E4], dur=0.25)
        .sound("guitar")
        .room(0.2)
    ]
)

# Drums
drums = stack(
    [
        loop([1,0,0,1,1,0,1,0]).sound("hi_hat"),  
        loop([0,0,1,0,0,1,0,0]).sound("snare").room(0.1),
        loop([1,0,0,0,1,0,0,0]).sound("kick")
    ]
)

# Bassline
bass = seq([C2, C2, E2, G2, C2, G2, E2, C2], dur=0.5).sawtooth().room(0.2)

# Combine everything and play
final_stack = stack([melody, drums, bass])
final_stack.play()   # <-- This is necessary
