`define ROWS 256
`define COLS 64

module top(
  input i_clk,
  input i_reset_n,
  input [`ROWS-1:0] [31:0] i_col_val,
  input [`COLS-1:0] [31:0] i_row_val,
  output [31:0] o_val
);




wire [63:0] [31:0] sum_out;

genvar rr, cc;
generate
  for (rr=0; rr<`ROWS; rr=rr+1) begin : gen1
    for (cc=0; cc<`COLS; cc=cc+1) begin : gen2
      example_module example(
        .i_clk      (i_clk),
        .i_reset_n  (i_reset_n),
        .i_a          (i_row_val[rr]),
        .i_b          (i_col_val[cc]),
        .o_sum        ()
      );
      end
    end
endgenerate
endmodule


module example_module(
  input i_clk,
  input i_reset_n,
  input [31:0] i_a,
  input [31:0] i_b,
  output [31:0] o_sum
);
/*verilator no_inline_module*/

  wire [31:0] sum, mult;
  logic [3:0] [31:0] flops, flops_next;

  assign o_sum = flops[3];


  assign sum = i_a + i_b;
  assign mult = i_a * i_b;
  always_ff @(posedge i_clk) begin
    if (~i_reset_n) begin
      flops <= 0;
    end else begin
      flops <= flops_next;
    end
  end

  always_comb begin
    flops_next[0] = sum;
    flops_next[1] = mult;
    flops_next[2] = flops[0] ^ flops[1];
    flops_next[3] = flops[3] + flops[2];
  end
endmodule



