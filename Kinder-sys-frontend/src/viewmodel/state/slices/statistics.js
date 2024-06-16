import { createSlice } from "@reduxjs/toolkit";

const statisticsInitialState = {
  year: 2023,
  groupId: 1,
};

const statistics = createSlice({
  name: "statistics",
  initialState: statisticsInitialState,
  reducers: {
    setGroupId: (state, action) => {
      state.groupId = action.payload;
    },
    setYear: (state, action) => {
      state.year = action.payload;
    },
  },
});

export const { setGroupId, setYear } = statistics.actions;

export const statisticsReducer = statistics.reducer;
