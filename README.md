## Simulated Annealing
This is a homework project from my study group AI laboratory. Kindly read about [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
                                ![example from wikipedia](https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif)</br>
credit gif : [wikipedia](https://en.wikipedia.org/)


## Breakdown
This project are my initial version.
the purpose of this project is to find the lowest result of this function :
![function](https://github.com/ahsanatha/AI-Simulated-Annealing/blob/master/img/function.png)

Initial Temperature is 2000000000000.
and The Cooling Rate is 0.000001

### Hypothesis
i assume that if you make cooling rate greater than 0.5 you will make the program infinity loop.
Because we are using float as variable type.
    [!] update : this is not a infinity loop. when you make Cooling Rate greater than 0.5, its harder to Tawal to reach 0 since there is an infinite floating number before reach 0. So i changed Takhir to 0.000001. And modify the cooling rate so there will be a lot of process going on before reach the lowest temperature.


## Result
![result](https://github.com/ahsanatha/AI-Simulated-Annealing/blob/master/img/Result.png)

## Conclusion
So, if you try to run this program repeatedly, you will realize that the answer is always around
```
-0.044
```
so i jumped into my conlusion that the minimum result is **-0.044**

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Muhammad Ahsan Athallah](#)

p.s. Am also still workin on my english grammar. Sorry for Grammar Nazy's out there.
