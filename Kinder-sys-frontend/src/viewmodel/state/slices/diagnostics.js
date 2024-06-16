import { createSlice } from "@reduxjs/toolkit";

const diagnosticsInitialState = {
  groupId: 1,
  diagnosticsList: [],
};

const diagnostics = createSlice({
  name: "diagnostics",
  initialState: diagnosticsInitialState,
  reducers: {
    setGroupId: (state, action) => {
      state.groupId = action.payload;
    },
    updateDiagnosticsList: (state, action) => {
      state.diagnosticsList = action.payload;
    },
  },
});

export const { setGroupId, updateDiagnosticsList } = diagnostics.actions;

export const diagnosticsReducer = diagnostics.reducer;
