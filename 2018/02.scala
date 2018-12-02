import scala.io.Source

object Solve02 {
  def main(args: Array[String]) {
    var ids = Source.fromFile("02.in").mkString.split("\n")

    var freqs = ids.map(
      id => id.foldLeft(Map.empty[Char, Int]) { (map, k) =>
        map + (k -> (map.getOrElse(k, 0) + 1))
      })

    var twos_and_threes = freqs.foldLeft(Map.empty[Int, Int]) { (map, id) =>
      map + (
        2 -> (map.getOrElse(2, 0) + (if (id.values.exists(_ == 2)) 1 else 0)),
        3 -> (map.getOrElse(3, 0) + (if (id.values.exists(_ == 3)) 1 else 0))
      )
    }

    println(twos_and_threes(2) * twos_and_threes(3))

    // assume same length
    def almost_equal(x: String, y: String): Boolean = {
      x.length == y.length &&
      x.zip(y).count(pair => pair._1 == pair._2) == x.length - 1
    }

    var found = ids
      .flatMap(x => ids.map(y => (x, y)))
      .find(tuple => almost_equal(tuple._1, tuple._2)
    )
    var (x, y) = found.get
    var common = x.zip(y).foldLeft("") { (result, tuple) =>
      result + (if (tuple._1 == tuple._2) tuple._1 else "")
    }
    println(common)
  }
}
