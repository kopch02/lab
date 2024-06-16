import { createSlice } from "@reduxjs/toolkit";

const recommendationsInitialState = {
  categoryId: 1,
  groupId: 1,
};

const recommendations = createSlice({
  name: "recommendations",
  initialState: recommendationsInitialState,
  reducers: {
    setCategoryId: (state, action) => {
      state.categoryId = action.payload;
    },
    setGroupId: (state, action) => {
      state.year = action.payload;
    },
  },
});

export const { setCategoryId, setGroupId } = recommendations.actions;

export const recommendationsReducer = recommendations.reducer;
