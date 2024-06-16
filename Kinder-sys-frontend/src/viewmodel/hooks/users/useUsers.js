import { useDispatch, useSelector } from "react-redux";
import { setLogin, setRole } from "../../state/slices/user";

const useUser = () => {
  const dispatch = useDispatch();
  const { login, role } = useSelector((state) => state.user);

  const handleLoginChange = (login) => {
    dispatch(setLogin(login));
  };

  const handleRoleChange = (role) => {
    dispatch(setRole(role));
  };

  return {
    login,
    role,
    handleLoginChange,
    handleRoleChange,
  };
};

export default useUser;
