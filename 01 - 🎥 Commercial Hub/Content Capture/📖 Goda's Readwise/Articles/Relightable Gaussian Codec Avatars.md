# Relightable Gaussian Codec Avatars

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata
- Author: [[shunsukesaito.github.io]]
- Full Title: Relightable Gaussian Codec Avatars
- Category: #articles
- URL: https://shunsukesaito.github.io/rgca/
- Tags:

## Highlights
- In this work, we present Relightable Gaussian Codec Avatars, a method to build high-fidelity relightable head avatars that can be animated to generate novel expressions.
  Our geometry model based on 3D Gaussians can capture 3D-consistent sub-millimeter details such as hair strands and pores on dynamic face sequences. To support diverse materials of human heads such as the eyes, skin, and hair in a unified manner, we present a novel relightable appearance model based on learnable radiance transfer. Together with global illumination-aware spherical harmonics for the diffuse components, we achieve real-time relighting with all-frequency reflections using spherical Gaussians. This appearance model can be efficiently relit in real-time under both point light and continuous illumination. We further improve the fidelity of eye reflections and enable explicit gaze control by introducing relightable explicit eye models.
  Our method outperforms existing approaches without compromising real-time performance. We also demonstrate real-time relighting of avatars on a tethered consumer VR headset, showcasing the efficiency and fidelity of our avatars. ([View Highlight](https://read.readwise.io/read/01hh38cerxeamq0cwjapv2x79w))
- Relightable Gaussian Codec Avatars are conditioned with a latent expression code, gaze information, and a target view direction. The underlying geometry is parameterized by 3D Gaussians and can be efficiently rendered with the Gaussian Splatting technique. To enable efficient relighting with various illuminations, we present a novel learnable radiance transfer based on diffuse spherical harmonics and specular spherical Gaussians. Please refer to the paper for more details. ([View Highlight](https://read.readwise.io/read/01hh38eymc24azrahpqn18ma0v))
    - Note: This is interesting
