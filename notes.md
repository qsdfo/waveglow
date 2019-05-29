# Wavetable

## Steps
1- Generate individual grains.
 Observe:
	- if it's easy to concatenate them (olap)
 	- if it's easy to pitch shift them
 	- diversity of sampling
 	- structure of latent

2- Then try to draw continuous paths in the latent space as a wavetbale synth would do it

## Issues 
- aliasing when pitch increases (should be implemented in standard wavetables)
- flag for conditioning on attack, decay, release ? Or just envelope on amplitude ?

## Database
- https://www.soundsnap.com/
- https://www.soundsnap.com/tags/synth?page=182

## Biblio
https://nips2018creativity.github.io/doc/neural_wavetable.pdf 

# Waveglow

## Tests
- generate music with pre-trained model ?
    - works okay (small artifacts)
- remove conditioning, train on SOL
- conditioning spectral features
- VarNet / Glow

## Ideas
Probablement il faudra générer des waveforms plus longues que juste un cycle. Plutôt genre 4-5 cycles

## Synthese wavetable
- osc_gen
    - generate Wav qui parcourt la wavetable. Dans ce cas créer des wavetables suffisemment grande (sinon le wav dure deux secondes)
- serum
    - generer des wav et les uploader dans serum à la main