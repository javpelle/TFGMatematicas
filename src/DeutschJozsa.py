from qiskit import *
class DeutschJozsa:
        
    def create_circuit(self, uf, q = 5):
        """ Creates a new Deutsch-Jozsa circuit.
        Args:
            uf: quantum gatearray of f
            q: total system qubits
        """
        qr = QuantumRegister(q)
        cr = ClassicalRegister(q - 1)
        qc = QuantumCircuit(qr, cr)
        
        # Last qubit negation
        qc.x(qr[-1])
        qc.barrier()
        # Hadamard gate to each qubit
        for q in qr:
            qc.h(q)
        qc.barrier()
        # U_f
        uf(qc, qr)
        qc.barrier()
        # Hadamard gate to first q-1 qubits
        for q in qr[:-1]:
            qc.h(q)
        qc.barrier()  
        # Measure first q-1 qubits
        qc.measure(qr[:-1], cr)
        self.qc = qc
    
    def run(self, backend = Aer.get_backend('qasm_simulator'), shots = 1):
        """ Runs Deutsch-Jozsa circuit.
        Args:
            backend: Backend to execute circuits on.
                Default: Aer.get_backend('qasm_simulator')
            shots: Number of repetitions of each circuit, for sampling.
                Default: 1
        """
        self.shots = shots
        self.ex = execute(self.qc, backend = backend, shots = shots)
    
    def get_result(self):
        """ Returns string 'constant' if f is constant. 'balanced' if f is
                balanced.
        """
        try:
            if self.shots == 1:
                s = next(iter(self.ex.result().get_counts()))
                if all([x == '0' for x in s]):
                    return 'constant'
                else:
                    return 'balanced'
            else:
                print('Multiple enhanced executions')
        except:
            print('Call run(...)')
                
    
    def get_circuit(self):
        try:
            return self.qc
        except:
            print('Circuit does not exist. Call create_circuit(...)')
    
    def get_counts(self):
        return self.ex.result().get_counts()
                
    def uf_balanced(qc, qr):
        """ f(x_1,...)=1 if x_1=1. 0 otherwiswe (balanced).
        """
        qc.cx(qr[0], qr[-1])
        
    def uf_constant(qc, qr):
        """ f(x_1,...)=1 (constant).
        """
        qc.x(qr[-1])