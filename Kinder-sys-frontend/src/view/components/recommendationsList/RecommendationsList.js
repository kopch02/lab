import useRecommendations from "../../../viewmodel/hooks/recommendations/useRecommendations";
import Recommendation from "./recommendation/Recommendation";

import s from "./RecommendationList.module.scss";

const RecommendationsList = () => {
  const { recommendationsData } = useRecommendations();

  return (
    <div className={s.recommendations_list}>
      {recommendationsData.map(
        (
          {
            category,
            highScoreRecommendation,
            middleScoreRecommendation,
            lowScoreRecommendation,
          },
          index,
        ) => (
          <Recommendation
            key={index}
            category={category.name}
            high={highScoreRecommendation}
            mid={middleScoreRecommendation}
            low={lowScoreRecommendation}
          />
        ),
      )}
    </div>
  );
};

export default RecommendationsList;
