University of System Assignment

**Acorn Runner**

You are an acorn, heir to the Honourable Furious Forest Throne. Your beauty shines like no other, reﬂecting the colourful solar rays into the eyes of all spectators. But instead of your usual coat of beautiful acorn shell, you ﬁnd yourself covered in ash. Not only that, but you've fallen great depths from the heights of the towering trees of the Honourable Furious Forest that once cared for you.

You shed a tear of loss. The horrid memories of the Fire Nation's invasion ﬂash before you as you relive the moments your hometown, the Honourable Furious Forest, was burnt to ashes. Your friends, the koalas and kangaroos, your family, the Honourable Furious Forest members, all burnt to a crisp.

Mustering up your motivation for revenge, you, the acorn, heir to the Honourable Furious Forest Throne, stumble forward and ﬁnd yourself in a maze. You observe walls of ﬁre, helicopter search lights and teleporting pads within.

You cry out and slam your little acorn ﬁst on the greyed Honourable Furious Forest ﬂoor of dried up leaves. You swear upon your Father's name, Lord Scarlet Oak of the Honourable Furious Forest, that you will conquer this maze and restore the Honourable Furious Forest back to its former glory of rainbow and sunshine.



**Description**

In this assignment there will be three parts:

A game component. You must be able to play the game yourself.

The game will be a 2D maze with the objective of moving from start to end.

A solver component.

It should play the game as many times as it needs to generate a successful path.

More on this in the Solver section of this speciﬁcation.

| Cell character       | Meaning                                                      |
| -------------------- | ------------------------------------------------------------ |
| A                    | Player cell (stands for Acorn)                               |
| ' '                  | Air cell (space bar)                                         |
| X                    | Starting cell                                                |
| Y                    | Ending/Goal cell                                             |
| *                    | Wall cells                                                   |
| 1, 2, 3, 4,5,6,7,8,9 | Teleport cells. These numbers will come in pairs. On stepping onto the cell,you enter the cell '1', you teleport to the other '1'. Values greater than 9 will not be given. Note: 0 is not a valid teleport pad! |
| W                    | A water bucket cell. On stepping onto the cell, the player gains a water bucket. |
| F                    | A ﬁre obstacle that you cannot pass unless you have a water bucket. |

**Conﬁguration**

There will be one txt ﬁle which contains an ASCII representation of the maze. The maze may have more than one viable solution. The symbols correspond to the cell characters outlined above. All letters shall be in upper case.

Example conﬁguration ﬁle:

![image-20210726114314516](\screenshot\image-20210726114314516.png)





**Commands**

| Command | Meaning       |
| ------- | ------------- |
| w       | Move up       |
| a       | Move left     |
| s       | Move down     |
| d       | Move right    |
| e       | Wait a turn   |
| q       | Quit the game |



If the user enters an invalid move, print Please enter a valid move (w, a, s, d, e, q)..

The game should then continue to ask for the next move.

These commands are case-insensitive!

 you if you want to use it!



 Usage: python3 run.py  <filename>



![image-20210726114739641](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114739641.png)

![image-20210726114810077](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114810077.png)

![image-20210726114830831](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114830831.png)

![image-20210726114858460](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114858460.png)

![image-20210726114920289](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114920289.png)

![image-20210726114943633](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114943633.png)

![image-20210726114959973](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726114959973.png)

![image-20210726115012736](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726115012736.png)

![image-20210726115029062](C:\Users\steve\AppData\Roaming\Typora\typora-user-images\image-20210726115029062.png)



For more information about this assignment, please look at Acorn Assignment v1.4.pdf. Thanks :)
