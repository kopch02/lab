import { useState } from "react";
import RecommendationsList from "../../components/recommendationsList/RecommendationsList";
import Selection from "../../components/selection/Selection";
import { Stats } from "../../components/stats/Stats";
import { MyButton } from "../../components/button/MyButton";
import { RecommendationForm } from "../../components/forms/RecommendationsFrom/RecommendationForm";

import s from "./AnalyticsPage.module.scss";

const AnalyticsPage = () => {
  const [isActive, setIsActive] = useState(false);

  const toggleActive = () => {
    setIsActive(!isActive);
  };

  // const { diagnosticsData } = useDiagnostics();

  return (
    <>
      <div className="flex flex-col gap-1">
        <div className="ml-auto mr-auto mt-2 flex-1">
          <Selection />
        </div>
        <div className="ml-auto mr-auto flex flex-row gap-10">
          <div className="flex flex-col gap-2">
            <div className="py-3">
              <Stats start_data={start_data} end_data={end_data} />
            </div>
          </div>
          <div
            className={`ml-auto mr-auto mt-2 flex-1 ${s.recommendation_container}`}
          >
            <RecommendationsList />
            <MyButton text="Добавить рекомндацию" func={toggleActive} />
            <RecommendationForm
              isactive={isActive}
              toggleactive={toggleActive}
            />
          </div>
        </div>
      </div>
    </>
  );
};

const start_data = [
  {
    count: 2,
    procent: "20%",
  },
  {
    count: 3,
    procent: "30%",
  },
  {
    count: 5,
    procent: "50%",
  },
];

const end_data = [
  {
    count: 0,
    procent: "0%",
  },
  {
    count: 1,
    procent: "10%",
  },
  {
    count: 9,
    procent: "90%",
  },
];
export default AnalyticsPage;
