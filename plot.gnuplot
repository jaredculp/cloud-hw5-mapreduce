set title "Tweet Sentiment During UVA Presidency Crisis"
set xlabel "Date"
set ylabel "Tweet Sentiment Score (normalized)"
set xdata time
set timefmt "%Y%m%d"
set xtics format "%b %d"
set terminal png size 900, 300
set output "chart.png"
set xrange ["20130616":"20130705"]
plot 'sullivan.dat' u 1:2 t 'Sullivan' w lines, 'dragas.dat' u 1:2 t 'Dragas' w lines