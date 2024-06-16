import { useDispatch, useSelector } from "react-redux";
import { useGetGroupsQuery } from "../../../transport/groups";

const useGroupes = () => {
  const dispatch = useDispatch();
  const { data: groupsData = [], isSuccess } = useGetGroupsQuery();

  return {
    groupsData,
    isSuccess,
  };
};

export default useGroupes;
