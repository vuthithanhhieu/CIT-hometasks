defmodule Primes do
  def isPrime(num) do
    (2..num
     |> Enum.filter(fn(x) -> rem(num, x) == 0 end)
     |> length()) == 1
  end

  def primes(n, _, counter) when counter == n + 1, do: []

  def primes(n, acc, counter) do
    if (isPrime(acc)), do: [acc | primes(n, acc + 1, counter + 1)], else: primes(n, acc + 1, counter)
  end

  def printFirstPrimes(n), do: Enum.each(primes(n, 2, 1), fn(x) -> IO.puts(x) end)
end

Primes.printFirstPrimes(1000)