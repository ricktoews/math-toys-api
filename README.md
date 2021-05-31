# math-toys-api
The idea on this is to provide certain specific kinds of math data.
All of these are currently GET calls.

Decimal Calculator
dc/:denom/:num - Description of decimal expansion.
{
	num: string,
	denom: string,
	period: string,
	non-repeating: string,
	period-half: string,
	complement: string,
	repeating: string
}

dc/:denom/:num/:base - Same as above, but with base specified.


Powers of Phi
phi/:power - A description of the specified power of phi.
{
	power: integer,
	sqrt_5_coef: integer,
	whole: integer,
	fib_approx: real
}

phi-list/:up-to-power - The above, for each power, from 1 to the one specified.

Pythagorean Triples
pythag/:c-minus-b - Where c - b has the specified value.

pythag-c/primes - For prime values of c.

pythag-c/:prime/powers - For powers of the specified prime value of c.

pythag-c/:prime/multiples - For multiples of the specified prime value of c.


