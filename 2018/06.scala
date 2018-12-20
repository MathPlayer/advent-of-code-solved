import scala.io.Source

object Solve06 {
  def main(args: Array[String]) {
    var file_input = Source.fromFile("06.in").mkString
    println(file_input)

   // var re = raw"(\d+), (\d+)".r

   // val coords = file_input.foldLeft(Array.empty[Tuple2[Int, Int]]) {
   //   (array, line) => {
   //     var re(x, y) = line
   //     array + (x, y)
   //   }
   // }
   // println(coords)

   // // compupte min and max for x and y
   // val min_x = coords.foldLeft(_._1 min _._1)
   // val max_x = coords.foldLeft(_._1 max _._1)
   // val min_y = coords.foldLeft(_._2 min _._2)
   // val max_x = coords.foldLeft(_._2 max _._2)
    // for every point between min, max
    // determine closest coord
    // count coords
    // result
  }
}
