from fastapi import FastAPI, Request, HTTPException

from automata.fa.dfa import DFA
from automata.pda.dpda import DPDA
from automata.fa.nfa import NFA

app = FastAPI()


@app.post("/dfa")
async def automata(request: Request):
    info = await request.json()

    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))
    input_tape = info.get("input_tape", "")

    if len(states) == 0:
        raise HTTPException(status_code=400, detail="states cannot be empty")

    if len(input_symbols) == 0:
        raise HTTPException(status_code=400, detail="input_symbols cannot be empty")

    if len(transitions) == 0:
        raise HTTPException(status_code=400, detail="transitions cannot be empty")

    if len(initial_state) == 0:
        raise HTTPException(status_code=400, detail="initial_state cannot be empty")

    if len(final_states) == 0:
        raise HTTPException(status_code=400, detail="final_states cannot be empty")

    if len(input_tape) == 0:
        raise HTTPException(status_code=400, detail="input_tape cannot be empty")

    # DFA que corresponde a todas as cadeias binárias que terminam num número ímpar de '1's
    dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
        )

    if dfa.accepts_input(input_tape):
        return {
            "MT": "DFA que corresponde a todas as cadeias binárias que terminam num número ímpar de '1's",
            "Input Tape": input_tape,
            "Result": "accepted"
        }
    else:
        return {
            "MT": "DFA que corresponde a todas as cadeias binárias que terminam num número ímpar de '1's",
            "Input Tape": input_tape,
            "Result": "rejected"
        }

@app.post("/dpda")
async def automata(request: Request):
        info = await request.json()

        states = set(info.get("states", []))
        input_symbols = set(info.get("input_symbols", []))
        stack_symbols = set(info.get("stack_symbols", []))
        transitions = dict(info.get("transitions", {}))
        initial_state = info.get("initial_state", "")
        initial_stack_symbol = info.get("initial_stack_symbol", "")
        final_states = set(info.get("final_states", []))
        acceptance_mode = info.get("acceptance_mode", "")
        input_tape = info.get("input_tape", "")

        if len(states) == 0:
            raise HTTPException(status_code=400, detail="states cannot be empty")

        if len(input_symbols) == 0:
            raise HTTPException(status_code=400, detail="input_symbols cannot be empty")

        if len(stack_symbols) == 0:
            raise HTTPException(status_code=400, detail="stack_symbols cannot be empty")

        if len(transitions) == 0:
            raise HTTPException(status_code=400, detail="transitions cannot be empty")

        if len(initial_state) == 0:
            raise HTTPException(status_code=400, detail="initial_state cannot be empty")

        if len(initial_stack_symbol) == 0:
            raise HTTPException(status_code=400, detail="initial_stack_symbol cannot be empty")

        if len(final_states) == 0:
            raise HTTPException(status_code=400, detail="final_states cannot be empty")

        if len(acceptance_mode) == 0:
            raise HTTPException(status_code=400, detail="acceptance_mode cannot be empty")

        if len(input_tape) == 0:
            raise HTTPException(status_code=400, detail="input_tape cannot be empty")

        # DPDA que corresponde a zero ou mais 'a's, seguido do mesmo número de 'b's (aceitando por estado final)
        dpda = DPDA(
            states=states,
            input_symbols=input_symbols,
            stack_symbols=stack_symbols,
            transitions=transitions,
            initial_state=initial_state,
            initial_stack_symbol=initial_stack_symbol,
            final_states=final_states,
            acceptance_mode=acceptance_mode
        )

        if dpda.accepts_input(input_tape):
            return {
                "MT": "DPDA que corresponde a zero ou mais 'a's, seguido do mesmo número de 'b's (aceitando por estado final)",
                "Input Tape": input_tape,
                "Result": "accepted"
            }
        else:
            return {
                "MT": "DPDA que corresponde a zero ou mais 'a's, seguido do mesmo número de 'b's (aceitando por estado final)",
                "Input Tape": input_tape,
                "Result": "rejected"
            }

@app.post("/nfa")
async def automata(request: Request):
        info = await request.json()

        states = set(info.get("states", []))
        input_symbols = set(info.get("input_symbols", []))
        transitions = dict(info.get("transitions", {}))
        initial_state = info.get("initial_state", "")
        final_states = set(info.get("final_states", []))
        input_tape = info.get("input_tape", "")

        if len(states) == 0:
            raise HTTPException(status_code=400, detail="states cannot be empty")

        if len(input_symbols) == 0:
            raise HTTPException(status_code=400, detail="input_symbols cannot be empty")

        if len(transitions) == 0:
            raise HTTPException(status_code=400, detail="transitions cannot be empty")

        if len(initial_state) == 0:
            raise HTTPException(status_code=400, detail="initial_state cannot be empty")

        if len(final_states) == 0:
            raise HTTPException(status_code=400, detail="final_states cannot be empty")

        if len(input_tape) == 0:
            raise HTTPException(status_code=400, detail="input_tape cannot be empty")

        # NFA que corresponde a cadeias de caracteres que começam com 'a', terminam com 'a' e não contêm 'b's consecutivo
        nfa = NFA(
            states=states,
            input_symbols=input_symbols,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )

        if nfa.accepts_input(input_tape):
            return {
                "MT": "NFA que corresponde a cadeias de caracteres que começam com 'a', terminam com 'a' e não contêm 'b's consecutivo",
                "Input Tape": input_tape,
                "Result": "accepted"
            }
        else:
            return {
                "MT": "NFA which matches strings beginning with 'a', ending with 'a', and containingno consecutive 'b's",
                "Input Tape": input_tape,
                "Result": "rejected"
            }
