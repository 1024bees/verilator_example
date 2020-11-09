regex = r"BRA__([0-9]*)__KET"
import re
compiled = re.compile(regex)
f = open("mod_dir/Vtop.cpp")
o = open("mod_dir/Vtop2.cpp", "w+")


generic_garbage = """
VL_INLINE_OPT void Vtop_example_module::__settle_virtual(Vtop__Syms* __restrict vlSymsp, int i, int j ) {
    Vtop* const __restrict vlTOPp VL_ATTR_UNUSED = vlSymsp->TOPp;
    // Body
    this->__PVT__flops_next[0U] = (vlTOPp->i_row_val[i] 
                                   + vlTOPp->i_col_val[j]);
    this->__PVT__flops_next[1U] = (vlTOPp->i_row_val[i] 
                                   * vlTOPp->i_col_val[j]);
    this->__PVT__flops_next[2U] = (this->__PVT__flops[0U] 
                                   ^ this->__PVT__flops[1U]);
    this->__PVT__flops_next[3U] = (this->__PVT__flops[3U] 
                                   + this->__PVT__flops[2U]);
}
"""





for line in f:
    a = re.findall(regex,line)
    if a:
        sf = line.find("settle")
        fidx, sidx = a[0], a[1]
        if sf != -1:
            newline = f"{line[:sf]}_settle_virtual(vlSymsp,{fidx},{sidx});\n"
            o.write(newline)
        else:
            o.write(line)
    else:
        o.write(line)

f2 = open("mod_dir/Vtop_example_module.h")
o2 = open("mod_dir/Vtop_example_module2.h")

added_settle = False
for line in f2:
    if not added_settle and "_settle" in line:
        o2.write(line)
        o2.write("void __settle_virtual(Vtop__Syms* __restrict vlSymsp, int i, int j );\n")
        add_settle = True
    else:
        o2.write(line)
f3 = open("mod_dir/Vtop_example_module.cpp")
o3 = open("mod_dir/Vtop_example_module2.cpp")
for line in f3:
    if "=====" in line:
        o3.write(line)
        o3.write(generic_garbage)
    else:
        o3.write(line)
