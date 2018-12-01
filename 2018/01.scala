import scala.io.Source

object Solve01 {
  def main(args: Array[String]) {
    var freqs = Source.fromFile("01.in").mkString.split("\n").map(_.toInt)
    println(freqs.reduce(_ + _))

    var found : Set[Int] = Set.empty

    var iter_count = 0
    var value = 0
    while (true) {
      iter_count += 1
      println(s"Iteration: $iter_count")
      for (f <- freqs) {
        value += f
        if (found(value)) {
          println(s"Second time reached: $value")
          System.exit(0)
        }
        found += value
      }
    }
  }
}
