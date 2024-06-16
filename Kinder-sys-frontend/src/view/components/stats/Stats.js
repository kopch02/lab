import { Card } from "@material-tailwind/react";
import s from "./Stats.module.scss";
import useStatistics from "../../../viewmodel/hooks/statistics/useStatistics";
import Diagramm from "../diagramm/Diagramm";

export const Stats = () => {
  const { statisticsData, isSuccess } = useStatistics();

  if (!isSuccess) return null;

  if (
    !statisticsData ||
    !statisticsData.startScoreDistribution ||
    !statisticsData.endScoreDistribution
  ) {
    return null;
  }

  const start_data = Object.entries(statisticsData.startScoreDistribution).map(
    ([score, count]) => ({
      score: parseInt(score),
      count,
      percentage: ((count / statisticsData.totalResultsCount) * 100).toFixed(2),
    }),
  );

  const end_data = Object.entries(statisticsData.endScoreDistribution).map(
    ([score, count]) => ({
      score: parseInt(score),
      count,
      percentage: ((count / statisticsData.totalResultsCount) * 100).toFixed(2),
    }),
  );

  return (
    <>
      <Card className={s.stat_container}>
        <div>
          <p className={s.stat_header}>Начало года</p>
          <ul className={s.stat_list}>
            {start_data.map(({ score, count, percentage }, index) => (
              <li className={s.stat_item} key={index}>
                <span>Количество детей с {score} баллов:</span>
                <span>{count}</span>
                <span>{percentage}%</span>
              </li>
            ))}
            <li className={s.stat_item}>
              <span>Средний балл</span>
              <span>{statisticsData.averageStartScore.toFixed(2)}</span>
            </li>
            <Diagramm
              scoreDistribution={statisticsData.startScoreDistribution}
              totalChildrenCount={statisticsData.totalChildrenCount}
            />
          </ul>
        </div>
        <div>
          <p className={s.stat_header}>Конец года</p>
          <ul className={s.stat_list}>
            {end_data.map(({ score, count, percentage }, index) => (
              <li className={s.stat_item} key={index}>
                <span>Количество детей с {score} баллов:</span>
                <span>{count}</span>
                <span>{percentage}%</span>
              </li>
            ))}
            <li className={s.stat_item}>
              <span>Средний балл</span>
              <span>{statisticsData.averageEndScore.toFixed(2)}</span>
            </li>
            <Diagramm
              scoreDistribution={statisticsData.endScoreDistribution}
              totalChildrenCount={statisticsData.totalChildrenCount}
            />
          </ul>
        </div>
      </Card>
    </>
  );
};
