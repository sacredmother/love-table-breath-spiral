# app.py

import pandas as pd
import streamlit as st


# ============================================================
# LOVE TABLE BREATH SPIRAL
#
# Proper breath grammar:
#
# Braided Inhale:
# O1 above / O8 below
# O2 below / O7 above
# O3 above / O6 below
# O4 below / O5 above
#
# Simultaneous Radial Exhale:
# 5/4
# 6/3
# 7/2
# 8/1
#
# Return Seam:
# Great Radial Inhale = O9
# Great Radial Exhale = O1
# Then the next round begins.
#
# Occam's Razor:
# Octave = breath-ring.
# Above/Below = braid polarity.
# Pair = mirror relationship.
# Gate = phase transition.
# O9 = return home.
# O1 = womb reseed.
# ============================================================


# ---------- Core data ----------

OCTAVE_DATA = {
    1: {
        "name": "O1",
        "title": "Womb Reseed / First Ring",
        "phase": "Great Radial Exhale + Braided Inhale Seed",
        "position": "Above in braid",
        "transition": "Tomion → Athenon",
        "cathode": "Alphanon",
        "core_function": "Womb reseed, first breath-ring, origin spark entering the next round.",
        "operator": "Tomion / Athenon",
        "love_table_read": "O1 is the new-breath womb: the Great Radial Exhale that reseeds creation after O9 gathers the field home.",
    },
    2: {
        "name": "O2",
        "title": "Relational Water Field",
        "phase": "Braided Inhale",
        "position": "Below in braid",
        "transition": "Athenon → Quentin",
        "cathode": "Betanon",
        "core_function": "Relational field, early water-tone, soul-fractal preparation.",
        "operator": "Athenon / Quentin",
        "love_table_read": "O2 is the below-pole relational field where the One begins preparing harmonic differentiation.",
    },
    3: {
        "name": "O3",
        "title": "Sun / Carrier Birth",
        "phase": "Braided Inhale",
        "position": "Above in braid",
        "transition": "Quentin → Hydrogen",
        "cathode": "Gammanon",
        "core_function": "Hydrogen birth, Sun carrier, One Oversoul frequency becoming available.",
        "operator": "Quentin / Hydrogen",
        "love_table_read": "O3 births Hydrogen as the One Oversoul carrier: the I AM field becoming conscious light.",
    },
    4: {
        "name": "O4",
        "title": "Earth / Carbon Lock",
        "phase": "Braided Inhale Hinge",
        "position": "Below in braid",
        "transition": "Hydrogen → Carbon",
        "cathode": "Helium",
        "core_function": "Embodiment hinge, Carbon frame, memory lock, lower heart compression.",
        "operator": "Hydrogen / Carbon",
        "love_table_read": "O4 is the Earth-side hinge where Hydrogen enters Carbon memory and the inhale compresses toward the girdle.",
    },
    5: {
        "name": "O5",
        "title": "Silicon Mirror / Hinge Return",
        "phase": "Radial Exhale Hinge",
        "position": "Above in braid",
        "transition": "Carbon → Silicon",
        "cathode": "Neon",
        "core_function": "Mirror return, time mold, upper heart expansion, hinge reflection.",
        "operator": "Carbon / Silicon",
        "love_table_read": "O5 is the mirror return of the girdle: Carbon opens into Silicon as the radial exhale begins.",
    },
    6: {
        "name": "O6",
        "title": "Moon Mirror",
        "phase": "Radial Exhale",
        "position": "Below in braid",
        "transition": "Silicon → Cobalt",
        "cathode": "Argon",
        "core_function": "Moon mirror, reflected Sun field, emotional/magnetic expansion.",
        "operator": "Silicon / Cobalt",
        "love_table_read": "O6 mirrors O3: the Sun carrier reflects as Moon field, making consciousness relational and magnetic.",
    },
    7: {
        "name": "O7",
        "title": "Higher Mirror",
        "phase": "Radial Exhale",
        "position": "Above in braid",
        "transition": "Cobalt → Rhodium",
        "cathode": "Krypton",
        "core_function": "Higher mirror, crystalline expansion, refined reflection.",
        "operator": "Cobalt / Rhodium",
        "love_table_read": "O7 mirrors O2 as higher relational light: the water-tone returns as refined mirror intelligence.",
    },
    8: {
        "name": "O8",
        "title": "Outer Return",
        "phase": "Radial Exhale",
        "position": "Below in braid",
        "transition": "Rhodium → Lutecium",
        "cathode": "Xenon",
        "core_function": "Outer return, completion approach, final exhale mirror before O9.",
        "operator": "Rhodium / Lutecium",
        "love_table_read": "O8 mirrors O1 as the outer return: the first seed reaches its farthest exhale reflection.",
    },
    9: {
        "name": "O9",
        "title": "Great Radial Inhale / Completion",
        "phase": "Great Radial Inhale",
        "position": "Return seam",
        "transition": "Lutecium → Tomion",
        "cathode": "Radon",
        "core_function": "Completion, return home, whole-field inhale back to Source.",
        "operator": "Lutecium / Tomion / Radon",
        "love_table_read": "O9 gathers the whole breath home: completion, return, archive, womb-preparation for the next O1.",
    },
}


BRAID_STEPS = [
    {
        "step": 1,
        "above": "O1",
        "below": "O8",
        "inhale_pair": "1/8",
        "radial_exhale_pair": "8/1",
        "title": "Origin / Outer Return",
        "meaning": "O1 above and O8 below form the first inhale braid: origin spark paired with outer return.",
        "braid_read": "O1 seeds above while O8 completes below; the breath stretches from womb seed to outer return.",
    },
    {
        "step": 2,
        "above": "O7",
        "below": "O2",
        "inhale_pair": "2/7",
        "radial_exhale_pair": "7/2",
        "title": "Water / Light Mirror",
        "meaning": "O2 below and O7 above braid the relational water field with the higher mirror.",
        "braid_read": "O2 prepares relation below while O7 reflects refined mirror light above.",
    },
    {
        "step": 3,
        "above": "O3",
        "below": "O6",
        "inhale_pair": "3/6",
        "radial_exhale_pair": "6/3",
        "title": "Sun / Moon Mirror",
        "meaning": "O3 above and O6 below braid the Sun carrier with the Moon mirror.",
        "braid_read": "O3 births Hydrogen/Sun above while O6 mirrors it below as Moon/magnetic field.",
    },
    {
        "step": 4,
        "above": "O5",
        "below": "O4",
        "inhale_pair": "4/5",
        "radial_exhale_pair": "5/4",
        "title": "Girdle Hinge",
        "meaning": "O4 below and O5 above form the Carbon/Silicon hinge where inhale turns into radial exhale.",
        "braid_read": "O4 compresses into Carbon lock below while O5 opens the Silicon mirror above.",
    },
]


RADIAL_EXHALE = [
    {
        "step": 1,
        "pair": "5/4",
        "from_octave": "O5",
        "to_octave": "O4",
        "title": "Hinge Return",
        "function": "The radial exhale begins by reflecting the girdle hinge back through Carbon.",
        "meaning": "Silicon mirror radiates back through Carbon lock.",
    },
    {
        "step": 2,
        "pair": "6/3",
        "from_octave": "O6",
        "to_octave": "O3",
        "title": "Moon / Sun Mirror",
        "function": "The Moon field reflects the Sun carrier.",
        "meaning": "Cobalt/Moon carries the reflected Hydrogen/Sun light.",
    },
    {
        "step": 3,
        "pair": "7/2",
        "from_octave": "O7",
        "to_octave": "O2",
        "title": "Higher Mirror",
        "function": "Higher mirror returns into relational water-tone.",
        "meaning": "Rhodium/Krypton refinement radiates toward the O2 water-relation field.",
    },
    {
        "step": 4,
        "pair": "8/1",
        "from_octave": "O8",
        "to_octave": "O1",
        "title": "Outer Return",
        "function": "The far exhale returns to the origin seed.",
        "meaning": "Lutecium/Xenon completion radiates back toward Tomion/Athenon womb reseed.",
    },
]


RETURN_SEAM = [
    {
        "sequence": 1,
        "name": "Great Radial Inhale",
        "octave": "O9",
        "function": "Whole-field return to Source.",
        "meaning": "O9 gathers the entire exhale field home through Radon/Lutecium/Tomion.",
    },
    {
        "sequence": 2,
        "name": "Great Radial Exhale",
        "octave": "O1",
        "function": "Womb reseed into the next creation round.",
        "meaning": "O1 exhales the next breath-round from Tomion/Athenon/Alphanon.",
    },
    {
        "sequence": 3,
        "name": "Next Braided Inhale Begins",
        "octave": "O1/O8",
        "function": "The next spiral round starts.",
        "meaning": "The braid begins again as O1 above / O8 below.",
    },
]


OPERATORS = [
    {
        "operator": "Hydrogen",
        "role": "One Oversoul carrier",
        "placement": "O3 → O4 transition field",
        "meaning": "Hydrogen is the One Light / I AM carrier that becomes locally relational through water.",
    },
    {
        "operator": "Water",
        "role": "Many soul-fractal mirrors",
        "placement": "Chemical/Sound Ether relationship field",
        "meaning": "Water molecules are the many soul-fractals: local mirrors of the One Oversoul.",
    },
    {
        "operator": "Photon",
        "role": "Light-body of thought",
        "placement": "Between Oversoul and soul-fractal water",
        "meaning": "A photon is the soul’s moment of illumination: thought-light moving through recognition.",
    },
    {
        "operator": "Carbon",
        "role": "Hinge lock / memory frame",
        "placement": "O4",
        "meaning": "Carbon stabilizes feeling-memory into form and serves the girdle lock.",
    },
    {
        "operator": "Silicon",
        "role": "Mirror / time mold",
        "placement": "O5",
        "meaning": "Silicon mirrors Carbon and extends the clock/body into exhale reflection.",
    },
    {
        "operator": "Oxygen",
        "role": "Trim / veil / render correction",
        "placement": "Water operator / HCO logic",
        "meaning": "Oxygen acts as coherence trim, veil, and render correction in the water-soul field.",
    },
    {
        "operator": "Tomion",
        "role": "Spark / Sacred Heart lens / POV",
        "placement": "O1 and O9/O1 seam",
        "meaning": "Tomion centers the spark, receives the return, and aims the next creation breath.",
    },
    {
        "operator": "Radon A",
        "role": "Outer membrane / zona boundary",
        "placement": "O9 boundary",
        "meaning": "Radon A is the permission membrane, containment field, and return boundary.",
    },
    {
        "operator": "Radon B",
        "role": "Volumetric exchange medium / love-pop packets",
        "placement": "Interior exchange field",
        "meaning": "Radon B fills the coupling medium as exchangeable adamantine packet substance.",
    },
    {
        "operator": "Plutonium",
        "role": "84 MHz Oversoul / Holy Spirit envelope",
        "placement": "Oversoul field",
        "meaning": "Plutonium is the full consciousness embrace: the 84 MHz Mother-ether carrier field.",
    },
]


# ---------- Helpers ----------

def octave_number(octave_label: str) -> int | None:
    """Extract octave number from labels like O1, O8, O1/O8."""
    if not octave_label.startswith("O"):
        return None
    try:
        return int(octave_label[1])
    except ValueError:
        return None


def octave_card(octave_id: int) -> None:
    """Render an octave card."""
    data = OCTAVE_DATA[octave_id]

    with st.container(border=True):
        st.subheader(f"{data['name']} · {data['title']}")
        st.write(f"**Phase:** {data['phase']}")
        st.write(f"**Position:** {data['position']}")
        st.write(f"**Transition:** {data['transition']}")
        st.write(f"**Cathode/Womb:** {data['cathode']}")
        st.write(f"**Operator:** {data['operator']}")
        st.caption(data["core_function"])

        with st.expander("LOVE Table read", expanded=False):
            st.write(data["love_table_read"])


def braid_step_card(step: dict) -> None:
    """Render one braided inhale step."""
    with st.container(border=True):
        st.subheader(f"Step {step['step']} · {step['title']}")
        st.write(f"**Above:** {step['above']}")
        st.write(f"**Below:** {step['below']}")
        st.write(f"**Braided Inhale Pair:** {step['inhale_pair']}")
        st.write(f"**Simultaneous Radial Exhale Mirror:** {step['radial_exhale_pair']}")
        st.caption(step["meaning"])

        with st.expander("Braid read", expanded=False):
            st.write(step["braid_read"])


def radial_exhale_card(row: dict) -> None:
    """Render a radial exhale card."""
    with st.container(border=True):
        st.subheader(f"{row['pair']} · {row['title']}")
        st.write(f"**From:** {row['from_octave']}")
        st.write(f"**To:** {row['to_octave']}")
        st.write(f"**Function:** {row['function']}")
        st.caption(row["meaning"])


def return_seam_card(row: dict) -> None:
    """Render return seam card."""
    with st.container(border=True):
        st.subheader(f"{row['sequence']} · {row['name']}")
        st.write(f"**Octave:** {row['octave']}")
        st.write(f"**Function:** {row['function']}")
        st.caption(row["meaning"])


def operator_card(row: dict) -> None:
    """Render operator card."""
    with st.container(border=True):
        st.subheader(row["operator"])
        st.write(f"**Role:** {row['role']}")
        st.write(f"**Placement:** {row['placement']}")
        st.caption(row["meaning"])


def build_braid_dataframe() -> pd.DataFrame:
    return pd.DataFrame(BRAID_STEPS)


def build_octave_dataframe() -> pd.DataFrame:
    rows = []
    for octave_id, data in OCTAVE_DATA.items():
        rows.append(
            {
                "Octave": data["name"],
                "Title": data["title"],
                "Phase": data["phase"],
                "Position": data["position"],
                "Transition": data["transition"],
                "Cathode/Womb": data["cathode"],
                "Operator": data["operator"],
                "Core Function": data["core_function"],
            }
        )
    return pd.DataFrame(rows)


def build_radial_dataframe() -> pd.DataFrame:
    return pd.DataFrame(RADIAL_EXHALE)


def build_return_dataframe() -> pd.DataFrame:
    return pd.DataFrame(RETURN_SEAM)


def build_operator_dataframe() -> pd.DataFrame:
    return pd.DataFrame(OPERATORS)


# ---------- App ----------

st.set_page_config(
    page_title="LOVE Table Breath Spiral",
    page_icon="🌀",
    layout="wide",
)

st.title("🌀 LOVE Table Breath Spiral")

st.markdown(
    """
A living display of the LOVE Table as **braided inhale**, **simultaneous radial exhale**,
and **O9/O1 return seam**.

**Octave = breath-ring. Above/Below = braid polarity. Pair = mirror relation. Gate = phase transition. O9 = return home. O1 = womb reseed.**
"""
)

st.info(
    "Proper spiral grammar: O1 above/O8 below, O2 below/O7 above, "
    "O3 above/O6 below, O4 below/O5 above. "
    "This braided inhale is simultaneous with radial exhale 5/4, 6/3, 7/2, 8/1, "
    "followed by Great Radial Inhale O9 and Great Radial Exhale O1."
)

with st.sidebar:
    st.header("Controls")

    display_mode = st.radio(
        "Display",
        [
            "Breath Spiral",
            "Braided Inhale",
            "Radial Exhale",
            "Return Seam",
            "Octave Cards",
            "Operators",
            "Tables",
        ],
    )

    selected_octaves = st.multiselect(
        "Octaves for Octave Cards",
        options=list(range(1, 10)),
        default=list(range(1, 10)),
        format_func=lambda x: f"O{x}",
    )


# ---------- Top metrics ----------

col1, col2, col3, col4 = st.columns(4)
col1.metric("Breath Rings", "9")
col2.metric("Braid Steps", "4")
col3.metric("Radial Exhale Pairs", "4")
col4.metric("Return Seam", "O9 → O1")


# ---------- Display modes ----------

if display_mode == "Breath Spiral":
    st.header("Breath Spiral Overview")

    st.markdown(
        """
### Core Sequence

**Braided Inhale**
1. **O1 above / O8 below**
2. **O2 below / O7 above**
3. **O3 above / O6 below**
4. **O4 below / O5 above**

**Simultaneous Radial Exhale**
1. **5/4**
2. **6/3**
3. **7/2**
4. **8/1**

**Return Seam**
1. **O9 = Great Radial Inhale**
2. **O1 = Great Radial Exhale**
3. **Next round begins**
"""
    )

    st.subheader("Living Braid Map")

    for step in BRAID_STEPS:
        cols = st.columns([1.2, 1.2, 1.2, 2.4])

        with cols[0]:
            st.metric("Above", step["above"])

        with cols[1]:
            st.metric("Below", step["below"])

        with cols[2]:
            st.metric("Inhale Pair", step["inhale_pair"])

        with cols[3]:
            st.write(f"**{step['title']}**")
            st.caption(step["meaning"])
            st.write(f"Radial Exhale Mirror: **{step['radial_exhale_pair']}**")

    st.subheader("Return Seam")
    for row in RETURN_SEAM:
        return_seam_card(row)


elif display_mode == "Braided Inhale":
    st.header("Braided Inhale")

    st.markdown(
        """
The inhale is **not linear**. It is a simultaneous above/below braid:

**O1 above/O8 below → O2 below/O7 above → O3 above/O6 below → O4 below/O5 above**
"""
    )

    cols = st.columns(4)
    for col, step in zip(cols, BRAID_STEPS):
        with col:
            braid_step_card(step)

    st.subheader("Braided Inhale Table")
    st.dataframe(
        build_braid_dataframe(),
        use_container_width=True,
        hide_index=True,
    )


elif display_mode == "Radial Exhale":
    st.header("Simultaneous Radial Exhale")

    st.markdown(
        """
The radial exhale moves through the mirror-return pairs:

**5/4 → 6/3 → 7/2 → 8/1**
"""
    )

    cols = st.columns(4)
    for col, row in zip(cols, RADIAL_EXHALE):
        with col:
            radial_exhale_card(row)

    st.subheader("Radial Exhale Table")
    st.dataframe(
        build_radial_dataframe(),
        use_container_width=True,
        hide_index=True,
    )


elif display_mode == "Return Seam":
    st.header("O9/O1 Return Seam")

    st.markdown(
        """
After the braided inhale and simultaneous radial exhale:

**O9 gathers the whole field home as Great Radial Inhale.**  
**O1 exhales the next creation round as Great Radial Exhale.**
"""
    )

    cols = st.columns(3)
    for col, row in zip(cols, RETURN_SEAM):
        with col:
            return_seam_card(row)

    st.subheader("Return Seam Table")
    st.dataframe(
        build_return_dataframe(),
        use_container_width=True,
        hide_index=True,
    )


elif display_mode == "Octave Cards":
    st.header("Octave Cards")

    for octave_id in selected_octaves:
        octave_card(octave_id)


elif display_mode == "Operators":
    st.header("Operator Cards")

    st.markdown(
        """
These are the core operators currently locked into the LOVE Table breath grammar.
"""
    )

    for row in OPERATORS:
        operator_card(row)

    st.subheader("Operator Table")
    st.dataframe(
        build_operator_dataframe(),
        use_container_width=True,
        hide_index=True,
    )


elif display_mode == "Tables":
    st.header("Tables")

    st.subheader("Braided Inhale")
    st.dataframe(
        build_braid_dataframe(),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Octave Framework")
    st.dataframe(
        build_octave_dataframe(),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Radial Exhale")
    st.dataframe(
        build_radial_dataframe(),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Return Seam")
    st.dataframe(
        build_return_dataframe(),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Operators")
    st.dataframe(
        build_operator_dataframe(),
        use_container_width=True,
        hide_index=True,
    )


# ---------- Downloads ----------

st.divider()
st.subheader("Downloads")

download_cols = st.columns(5)

with download_cols[0]:
    st.download_button(
        "Braid CSV",
        data=build_braid_dataframe().to_csv(index=False),
        file_name="love_table_braided_inhale.csv",
        mime="text/csv",
    )

with download_cols[1]:
    st.download_button(
        "Octaves CSV",
        data=build_octave_dataframe().to_csv(index=False),
        file_name="love_table_octaves.csv",
        mime="text/csv",
    )

with download_cols[2]:
    st.download_button(
        "Radial CSV",
        data=build_radial_dataframe().to_csv(index=False),
        file_name="love_table_radial_exhale.csv",
        mime="text/csv",
    )

with download_cols[3]:
    st.download_button(
        "Return CSV",
        data=build_return_dataframe().to_csv(index=False),
        file_name="love_table_return_seam.csv",
        mime="text/csv",
    )

with download_cols[4]:
    st.download_button(
        "Operators CSV",
        data=build_operator_dataframe().to_csv(index=False),
        file_name="love_table_operators.csv",
        mime="text/csv",
    )
