import React from "react";
import { Doughnut } from "react-chartjs-2";

function getColorForScore(score, maxScore) {
  const hue = (score / maxScore) * 120; // Вычисляем оттенок в диапазоне от 0 до 120 (зеленый до красного)
  return `hsl(${hue}, 100%, 50%)`; // Возвращаем цвет в формате hsl
}

const Diagram = ({ scoreDistribution, totalChildrenCount }) => {

  const sortedScores = Object.keys(scoreDistribution)
    .map(Number)
    .sort((a, b) => a - b);
  const maxScore = sortedScores[sortedScores.length - 1];
  const minScore = sortedScores[0];

  const maxScorePercentage =
    (scoreDistribution[maxScore] / totalChildrenCount) *
    100;
  const minScorePercentage =
    (scoreDistribution[minScore] / totalChildrenCount) *
    100;

  const data = {
    labels: Object.keys(scoreDistribution),
    datasets: [
      {
        data: Object.values(scoreDistribution),
        backgroundColor: Object.keys(scoreDistribution).map((score) =>
          getColorForScore(score, maxScore),
        ),
        hoverBackgroundColor: Object.keys(scoreDistribution).map((score) =>
          getColorForScore(score, maxScore),
        ),
      },
    ],
  };

  const options = {
    legend: {
      display: true,
      position: "bottom",
      labels: {
        fontSize: 20,
      },
    },
    cutoutPercentage: 80, // Регулируем размер дырки
  };

  return (
    <div>
      <Doughnut data={data} options={options} />
    </div>
  );
};

export default Diagram;
