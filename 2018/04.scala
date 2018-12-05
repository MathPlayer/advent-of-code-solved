import scala.collection.immutable.ListMap
import scala.io.Source

object Solve04 {
  def main(args: Array[String]) {
    val lines = Source.fromFile("04.in").mkString.split("\n")
    val line_re = raw"\[\d+-(\d+)-(\d+) (\d+):(\d+)\] (.*)".r

    val raw_events = lines.foldLeft(Map.empty[Tuple4[Int, Int, Int, Int], Array[String]]) {
      (map, line) => {
        val line_re(month, day, hour, minute, raw_event) = line
        map + ((month.toInt, day.toInt, hour.toInt, minute.toInt) -> raw_event.split(" ").take(2))
      }
    }
    val sorted_events = ListMap(raw_events.toSeq.sortBy(_._1):_*)
    val (sleep_count, _, _) = sorted_events.foldLeft((Map.empty[Int, Map[Int, Int]], -1, -1)) {
      // acc is ((guard_id, (minute, sleep_count)), current_guard, last_sleep)
      (acc, entry) => {
        val (data, current_guard, current_minute) = acc
        val ((month, day, hour, minute), words) = entry

        if (words(0) == "Guard") {
          val guard = words(1).drop(1).toInt
          if (data.contains(guard)) {
            (data, guard, -1)
          } else {
            (data + (guard -> (for (m <- 0 to 59) yield (m, 0)).toMap), guard, -1)
          }
        } else if (words(0) == "falls") {
          (data, current_guard, minute)
        } else { // waking up
          val times = data(current_guard)
          (data +
            (current_guard -> times.foldLeft(Map.empty[Int, Int]) {
              (macc, mcount) =>
                macc + (mcount._1 -> (if (mcount._1 < minute && mcount._1 >= current_minute) mcount._2 + 1 else mcount._2))
            }), current_guard, -1)
        }
      }
    }

    // strategy 1
    val (sleepy_guard, _) = sleep_count.maxBy(_._2.values.sum)
    println(sleepy_guard * sleep_count(sleepy_guard).maxBy(_._2)._1)

    // strategy 2
    val (const_sleep_guard, _) = sleep_count.maxBy(_._2.values.reduceLeft(_ max _))
    println(const_sleep_guard * sleep_count(const_sleep_guard).maxBy(_._2)._1)

  }
}
