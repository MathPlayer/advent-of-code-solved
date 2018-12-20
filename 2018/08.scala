import scala.io.Source
import scala.collection.mutable.ArrayBuffer

object Solve06 {
  def main(args: Array[String]) {
    var file_input = Source.fromFile("08.in").mkString.split(" ").map(_.toInt)

    case class Node(children_count: Int, metadata_count: Int, children: ArrayBuffer[Node], metadata: Array[Int])


    def readNodes(input: Array[Int]): (Node, Array[Int]) = {
      var node = Node(input(0), input(1), ArrayBuffer.empty, input.takeRight(input(1)))
      for (x <- 0 to node.children_count) {
        var inner = input.drop(2).dropRight(node.metadata.length)
        println("reading inner length: " + inner.length)
        node.children += readNode(inner)
      }
      return node
    }

    var root = readNode(file_input)
    println(root.children_count)
    println(root.metadata_count)
    println(root.metadata)
  }
}
