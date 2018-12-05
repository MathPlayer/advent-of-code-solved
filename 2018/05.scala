import scala.collection.immutable.ListMap
import scala.io.Source

object Solve04 {
  def main(args: Array[String]) {
    var initial_polymer = Source.fromFile("05.in").mkString

    var re = raw"(aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ|Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz)".r

    def react(polymer: String): String = {
      var old_length = -1
      var final_polymer = polymer
      while (final_polymer.length != old_length) {
        old_length = final_polymer.length
        final_polymer = re.replaceAllIn(final_polymer, "")
      }
      return final_polymer
    }
    println(react(initial_polymer).length)

    for (x <- 'a' to 'z') {
      var remove_re = ("(" + x + "|" + x.toUpper + ")").r
      var improved_polymer = remove_re.replaceAllIn(initial_polymer, "")
      println("removing " + x + ": " + react(improved_polymer).length)
    }

  }
}
