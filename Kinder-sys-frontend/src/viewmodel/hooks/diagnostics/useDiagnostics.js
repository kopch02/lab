import { useDispatch, useSelector } from "react-redux";
import {
  setGroupId,
  updateDiagnosticsList,
} from "../../state/slices/diagnostics";
import { useGetDiagnosticsByGroupIdQuery } from "../../../transport/diagnostics";

const useDiagnostics = () => {
  const dispatch = useDispatch();
  const { groupId } = useSelector((state) => state.diagnostics);
  const { data: diagnosticsData = [] } =
    useGetDiagnosticsByGroupIdQuery(groupId);

  const handleGroupIdChange = (groupId) => {
    dispatch(setGroupId(groupId));
  };

  const handleDiagnosticsListUpdate = (diagnosticsList) => {
    dispatch(updateDiagnosticsList(diagnosticsList));
  };

  return {
    handleGroupIdChange,
    handleDiagnosticsListUpdate,
    diagnosticsData,
    groupId,
  };
};

export default useDiagnostics;
