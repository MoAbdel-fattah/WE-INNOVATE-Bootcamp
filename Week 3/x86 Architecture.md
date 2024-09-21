# **x86 Architecture**

- A central processing unit (CPU)—also called a central processor or main processor—is the most important processor in a given computer.Its electronic circuitry executes instructions of a computer program, such as arithmetic, logic, controlling, and input/output (I/O) operations. This role contrasts with that of external components, such as main memory and I/O circuitry,\[1\] and specialized coprocessors such as graphics processing units (GPUs).

## **CPU Components:**

- **Control Unit:** Fetches instructions from memory and controls their execution.  
- **Arithmetic Logic Unit (ALU):** Performs arithmetic and logical operations on data.  
- **Registers:** Small, high-speed storage locations within the CPU.  
- **Memory:** Stores program code and data.  
- **I/O Devices:** Interact with the computer, such as keyboards, mice, and displays.

### **Execution Process:**

1. **Instruction Fetch:** The Control Unit fetches the next instruction from memory using the Instruction Pointer (IP or RIP).  
2. **Instruction Decode:** The Control Unit decodes the instruction to determine the operation to be performed.  
3. **Data Fetch:** If necessary, the Control Unit fetches required data from memory or registers.  
4. **Operation Execution:** The ALU performs the specified operation on the data.  
5. **Result Storage:** The result is stored in a register or memory location.  
6. **Instruction Pointer Update:** The Control Unit updates the Instruction Pointer to the address of the next instruction.

## **CPU Registers**

- Registers are essential for efficient CPU operation.

### **Registers:**

* **CPU's Storage:** Registers are high-speed storage locations within the CPU.  
* **Quick Access:** Data access from registers is faster than from main memory.  
* **Limited Size:** Registers have a limited capacity compared to main memory.

#### **Types of Registers:**

* **Instruction Pointer (IP/EIP/RIP):** Stores the address of the next instruction to be executed.  
* **General-Purpose Registers:** Used for various purposes during program execution.  
  * **EAX/RAX:** Accumulator register for arithmetic operations.  
  * **EBX/RBX:** Base register for addressing offsets.  
  * **ECX/RCX:** Counter register for counting operations.  
  * **EDX/RDX:** Data register for multiplication/division.  
  * **ESP/RSP:** Stack pointer for stack operations.  
  * **EBP/RBP:** Base pointer for accessing stack parameters.  
  * **ESI/RSI:** Source index register for string operations.  
  * **EDI/RDI:** Destination index register for string operations.  
  * **R8-R15:** Additional general-purpose registers in 64-bit systems.

#### **Status and Segment Registers**

- **Status flags** provide information about the results of arithmetic and logical operations.  
- **Segment registers** are used to divide memory into segments for easier addressing.

##### **Status Flags:**

* **Zero Flag (ZF):** Set when the result of an operation is zero.  
* **Carry Flag (CF):** Set when the result of an operation overflows or underflows.  
* **Sign Flag (SF):** Set when the result of an operation is negative.  
* **Trap Flag (TF):** Enables single-stepping mode for debugging.

##### **Segment Registers:**

* **Code Segment (CS):** Points to the code section of the program.  
* **Data Segment (DS):** Points to the data section of the program.  
* **Stack Segment (SS):** Points to the stack section of the program.  
* **Extra Segments (ES, FS, GS):** Point to additional data sections.

## **Windows Memory Layout                                                                       Key Sections:**

* **Code:** Contains the program's executable instructions.  
* **Data:** Contains initialized data that remains constant.  
* **Heap:** Dynamically allocated memory for variables and data.  
* **Stack:** Stores local variables, function arguments, and return addresses.

### **Overview:**

* A program's memory is divided into these sections.  
* The layout of these sections may vary.  
* The stack is particularly important for malware analysis due to its role in control flow.

### **Stack:**

* Contains local variables, function arguments, and return addresses.  
* Targeted by malware to hijack control flow (e.g., buffer overflows).  
* Will be covered in more detail in the next task.