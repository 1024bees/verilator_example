import re

garbage = """

VL_INLINE_OPT void Vtop_example_module___settle_virtual(Vtop_example_module* vlSelf, int i, int j ) {
    if (false && vlSelf) {}  // Prevent unused
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+        Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__0__KET____DOT__gen2__BRA__0__KET____DOT__example__16385\n"); );
    // Body
    vlSelf->__PVT__flops_next[0U] = (vlSymsp->TOP.i_row_val[j] 
                                     + vlSymsp->TOP.i_col_val[i]);
    vlSelf->__PVT__flops_next[1U] = (IData)((((QData)((IData)(
                                                              (vlSelf->__PVT__flops[0U] 
                                                               ^ 
                                                               vlSelf->__PVT__flops[1U]))) 
                                              << 0x20U) 
                                             | (QData)((IData)(
                                                               (vlSymsp->TOP.i_row_val[j] 
                                                                * 
                                                                vlSymsp->TOP.i_col_val[i])))));
    vlSelf->__PVT__flops_next[2U] = (IData)(((((QData)((IData)(
                                                               (vlSelf->__PVT__flops[0U] 
                                                                ^ 
                                                                vlSelf->__PVT__flops[1U]))) 
                                               << 0x20U) 
                                              | (QData)((IData)(
                                                                (vlSymsp->TOP.i_row_val[j] 
                                                                 * 
                                                                 vlSymsp->TOP.i_col_val[i])))) 
                                             >> 0x20U));
    vlSelf->__PVT__flops_next[3U] = (vlSelf->__PVT__flops[3U] 
                                     + vlSelf->__PVT__flops[2U]);
}"""





def fix_settle(line: str) -> str:
    regex = r"BRA__([0-9]*)__KET"   
    res =re.findall(regex,line)
    i, j = res[0], res[1]
    self =f"&vlSymsp->TOP__top__DOT__gen1__BRA__{i}__KET____DOT__gen2__BRA__{j}__KET____DOT__example"
    newline = f"Vtop_example_module___settle_virtual({self},{i},{j});\n"
    return newline



test_str = """
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__4__KET____DOT__example__19973((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__4__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__5__KET____DOT__example__19974((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__5__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__6__KET____DOT__example__19975((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__6__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__7__KET____DOT__example__19976((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__7__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__8__KET____DOT__example__19977((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__8__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__9__KET____DOT__example__19978((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__9__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__10__KET____DOT__example__19979((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__10__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__11__KET____DOT__example__19980((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__11__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__12__KET____DOT__example__19981((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__12__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__13__KET____DOT__example__19982((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__13__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__14__KET____DOT__example__19983((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__14__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__15__KET____DOT__example__19984((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__15__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__16__KET____DOT__example__19985((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__16__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__17__KET____DOT__example__19986((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__17__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__18__KET____DOT__example__19987((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__18__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__19__KET____DOT__example__19988((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__19__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__20__KET____DOT__example__19989((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__20__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__21__KET____DOT__example__19990((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__21__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__22__KET____DOT__example__19991((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__22__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__23__KET____DOT__example__19992((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__23__KET____DOT__example));
Vtop_example_module___settle__TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__24__KET____DOT__example__19993((&vlSymsp->TOP__top__DOT__gen1__BRA__56__KET____DOT__gen2__BRA__24__KET____DOT__example));
"""


#regex = r"BRA__([0-9]*)__KET"
#import re
#compiled = re.compile(regex)
#for line in test_str.split('\n'):
#    if "Vtop_example_module___settle__TOP" in line:
#        print(fix_settle(line))
#
for filename in ["Vtop___024root__DepSet_h84412442__0.cpp", "Vtop___024root__DepSet_h84412442__1.cpp"]:
    temp_file = ""
    filepath = f"mod_dir/{filename}"
    file = open(filepath)
    for line in file:
        if "Vtop_example_module___settle__TOP" in line:
            temp_file += fix_settle(line)
        else:
            temp_file += line
    file.close()
    outfile = open(filepath, "w+")
    outfile.write(temp_file)


