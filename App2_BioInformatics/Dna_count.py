import pandas as pd
import streamlit as st
import altair as at
from PIL import Image

image = Image.open("dna-logo.png")
new_image = image.resize((600, 400))
st.image(new_image)

st.write(
    """
    # DNA Nucleotide Count Web App

    This app counts the nuleotide composition of DNA query!

"""
)

st.header("Enter DNA Sequence")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence Input",sequence_input,height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)
# sequence

st.write(
        """
***
"""
)

# st.header("Input DNA sequence")
# sequence

st.header("Output DNA")

##Print as Dictionary
st.subheader("1.Print Dictionary")

def DNA_nucleotide_count(seq):
    d = dict([
            ('A',seq.count('A')),
            ('G',seq.count('G')),
            ('T',seq.count('T')),
            ('C',seq.count('C'))
            ])
    return d

X = DNA_nucleotide_count(sequence)
X

st.write(
        """
***
"""
)

##Print in Text
st.subheader("2.Print text")

st.write("There are "+str(X['A'])+" adenine(A)")
st.write("There are "+str(X['T'])+" thymine(T)")
st.write("There are "+str(X['G'])+" guanine(G)")
st.write("There are "+str(X['C'])+" cytosin(C)")

st.write(
        """
***
"""
)

#Dataframe
st.subheader("3.Dataframe")

df = pd.DataFrame.from_dict(X,orient="index")
df = df.rename({0:"count"},axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index":"nucleotide"})
st.write(df)


##Display as Bar Chart
st.subheader("4.Bar Chart")
p = at.Chart(df).mark_bar().encode(
    x="nucleotide",
    y="count"
)

p = p.properties(
    width = at.Step(80)
)
st.write(p)