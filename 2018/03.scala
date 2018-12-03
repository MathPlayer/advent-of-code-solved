import scala.io.Source

object Solve03 {
  def main(args: Array[String]) {
    val input = Source.fromFile("03.in").mkString.split("\n")
    val re = raw"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)".r

    val patches = input.foldLeft(Map.empty[Int, Tuple4[Int, Int, Int, Int]]) {
      (map, line) => {
        val re(id, x, y, l, h) = line
        map + (id.toInt -> (x.toInt, y.toInt, l.toInt, h.toInt))
      }
    }

    val patch_map = patches.foldLeft(Map.empty[Tuple2[Int, Int], Int]) {
      case (map, (k, v)) => {
        var aux = Map.empty[Tuple2[Int, Int], Int]
        for (x <- v._1 to v._1 + v._3 - 1) {
          for (y <- v._2 to v._2 + v._4 - 1) {
            aux += ((x, y) -> (map.getOrElse((x, y), 0) + 1))
          }
        }
        map ++ aux
      }
    }

    println(patch_map.valuesIterator.count(_ >= 2))

    def patch_intact(id: Int, x: Int, y: Int, w: Int, h: Int, values:Map[Tuple2[Int, Int], Int]): Boolean = {
      var intact = true
      var i = x
      while (i < x + w && intact == true) {
        var j = y
        while (j < y + h && intact == true) {
          if (values.getOrElse((i,j), 0) > 1) {
            intact = false
          }
          j += 1
        }
        i += 1
      }
      return intact
    }

    println(patches.find({
      case (x, y) => patch_intact(x, y._1, y._2, y._3, y._4, patch_map)
    }))

  }
}
