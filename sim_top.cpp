
#include <verilated.h>

#include "Vtop.h"

//zipcpu s a 
template<class MODULE>	struct TESTBENCH {
	unsigned long	m_tickcount;
	MODULE	*m_core;

	TESTBENCH(void) {
		m_core = new MODULE;
		m_tickcount = 0l;
	}

	virtual ~TESTBENCH(void) {
		delete m_core;
		m_core = NULL;
	}

	virtual void	reset(void) {
		m_core->i_reset_n = 0;
		// Make sure any inheritance gets applied
		this->tick();
		m_core->i_reset_n = 1;
	}

	virtual void	tick(void) {
		// Increment our own internal time reference
		m_tickcount++;

		// Make sure any combinatorial logic depending upon
		// inputs that may have changed before we called tick()
		// has settled before the rising edge of the clock.
		m_core->i_clk = 0;
		m_core->eval();

		// Toggle the clock

		// Rising edge
		m_core->i_clk = 1;
		m_core->eval();

		// Falling edge
		m_core->i_clk = 0;
		m_core->eval();
	}
};



int main() {

  auto top_tb = new TESTBENCH<Vtop>();
  for(int i = 0; i < 100000; i++) {
    top_tb->tick();
  }


}
