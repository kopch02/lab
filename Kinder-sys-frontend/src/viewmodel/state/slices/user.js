import { createSlice } from "@reduxjs/toolkit";

const userInitialState = {
  login: "login",
  role: "admin1",
};

const user = createSlice({
  name: "user",
  initialState: userInitialState,
  reducers: {
    setLogin: (state, action) => {
      state.login = action.login;
    },
    setRole: (state, action) => {
      state.role = action.role;
    },
  },
});

export const { setLogin, setRole } = user.actions;

export const userReducer = user.reducer;
