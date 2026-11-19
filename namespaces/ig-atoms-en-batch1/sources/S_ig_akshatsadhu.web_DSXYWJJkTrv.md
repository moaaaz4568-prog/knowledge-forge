---
type: source
topic: instagram-transcripts
origin: "instagram-reels-texts/transcripts/akshatsadhu.web/DSXYWJJkTrv.txt"
words: 140
account: akshatsadhu.web
lang: en
quality: transcript
---

# S_ig_akshatsadhu.web_DSXYWJJkTrv

> مصدر خام — نسخة حرفية كاملة (شاهد read-only).
> الأصل: `instagram-reels-texts/transcripts/akshatsadhu.web/DSXYWJJkTrv.txt` — حساب: akshatsadhu.web — إنستجرام — فيديو DSXYWJJkTrv

---

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_STEPS 100
#define MAX_STEPS_PER_TURN 10

int main() {
    int steps = 0;
    int steps_per_turn = 0;
    int direction = 0; // 0 = forward, 1 = backward
    int turn = 0; // 0 = left, 1 = right
    int turn_direction = 0; // 0 = clockwise, 1 = counterclockwise
    int turn_steps = 0;

    srand(time(NULL));

    while (steps < MAX_STEPS) {
        steps_per_turn = rand() % MAX_STEPS_PER_TURN + 1;
        direction = rand() % 2;
        turn = rand() % 2;
        turn_direction = rand() % 2;
        turn_steps = rand() % MAX_STEPS_PER_TURN + 1;

        if (direction == 0) {
            printf("Move forward %d steps\n", steps_per_turn);
        } else {
            printf("Move backward %d steps\n", steps_per_turn);
        }

        if (turn == 0) {
            printf("Turn left %d steps\n", turn_steps);
        } else {
            printf("Turn right %d steps\n", turn_steps);
        }

        steps += steps_per_turn;
    }

    return 0;
}