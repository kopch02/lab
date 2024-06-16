import { useDispatch, useSelector } from "react-redux";
import { useGetRecommendationsByGroupIdQuery } from "../../../transport/recommendations";
import { setCategoryId, setGroupId } from "../../state/slices/recommendations";

const useRecommendations = () => {
  const dispatch = useDispatch();

  const { categoryId, groupId } = useSelector((state) => state.recommendations);
  const { data: recommendationsData = [] } =
    useGetRecommendationsByGroupIdQuery(groupId);

  const handleCategoryIdChange = (categoryId) => {
    dispatch(setCategoryId(categoryId));
  };

  const handleGroupIdChange = (groupId) => {
    dispatch(setGroupId(groupId));
  };

  return {
    handleCategoryIdChange,
    handleGroupIdChange,
    recommendationsData,
    categoryId,
    groupId,
  };
};

export default useRecommendations;
